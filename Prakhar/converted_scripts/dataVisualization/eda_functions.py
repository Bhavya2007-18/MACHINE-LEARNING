# eda_functions.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a consistent style for all plots
sns.set_style("whitegrid")

# 1. DATA LOADING FUNCTION
def load_data(file_path):
    """
    Loads the dataset from a given file path.
    Adjusts for the fact the original path was Windows-specific.
    """
    df = pd.read_csv(file_path)
    
    # Create the 'activity_bin' column if the original column exists
    if 'daily_active_minutes_instagram' in df.columns:
        df["activity_bin"] = pd.cut(
            df["daily_active_minutes_instagram"],
            bins=[0, 100, 200, 300, 400, 500],
            labels=["0–100", "100–200", "200–300", "300–400", "400–500"]
        )

    # Note: 'df_filtered' from the original script is undefined.
    # We'll handle age filtering inside a specific function later.
    return df

# 2. BASIC DATA INFO FUNCTION
def get_basic_info(df):
    """Returns basic dataframe info as strings for display."""
    buffer = []
    buffer.append(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    buffer.append("\n--- First 5 Rows ---")
    buffer.append(df.head().to_string())
    buffer.append("\n--- Column Names ---")
    buffer.append(", ".join(df.columns))
    buffer.append("\n--- Summary Statistics ---")
    buffer.append(df.describe().to_string())
    buffer.append(f"\n--- Missing Values ---\n{df.isna().sum().to_string()}")
    return "\n".join(buffer)

# 3. VISUALIZATION FUNCTIONS (One per plot from the original script)
def plot_activity_distribution(df):
    """Histogram of daily active minutes."""
    if 'daily_active_minutes_instagram' not in df.columns:
        return None
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['daily_active_minutes_instagram'], bins=20, kde=True, ax=ax)
    ax.set_title("Distribution of Daily Active Minutes on Instagram", fontsize=14)
    ax.set_xlabel("Daily Active Minutes", fontsize=12)
    ax.set_ylabel("User Count", fontsize=12)
    return fig

def plot_activity_by_gender(df):
    """Count plot of activity bins by gender."""
    if 'activity_bin' not in df.columns or 'gender' not in df.columns:
        return None
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x="gender", hue="activity_bin", ax=ax)
    ax.set_title("Instagram Activity by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("User Count")
    ax.legend(title="Daily Active Minutes")
    return fig

#this function was modified, undo this one to fix stuff incase everything breaks
def plot_reels_by_activity(df):
    """Bar plot: average reels watched per activity bin."""
    # ... (Implement similar to above for the 'reels_watched_per_day' plot)
    # Use the original plotting code but ensure it returns 'fig'
    if 'activity_bin' not in df.columns or 'reels_watched_per_day' not in df.columns:
        return None
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(data=df, x='activity_bin',y="reels_watched_per_day", estimator='mean', ax=ax)
    for p in ax.patches:
        height = p.get_height()
        if not np.isnan(height):
            ax.annotate(
                f'{height:.2f}',
                (p.get_x()+p.get_width()/ 2., height),
                ha='center',
                va='bottom',
                xytext=(0, 5),
                textcoords='offset points',
                fontsize=10,
                fontweight='bold',
                color='black'
            )
    ax.set_title("Average Reels Watched per Day by Activity")
    ax.set_ylabel("Averyage Reels Watcged per Day")
    ax.set_xlabel("Daily Active Minutes")
    return fig

def plot_activity_by_age(df, bin_size=5):
    """
    Bar plot: Instagram Activity by Age Groups.
    Groups ages into bins (default 5-year groups).
    """
    # Check required columns
    if 'daily_active_minutes_instagram' not in df.columns or 'age' not in df.columns:
        return None
    
    # Create a working copy to avoid modifying original
    plot_df = df.copy()
    
    # 1. Create age bins
    min_age = plot_df['age'].min()
    max_age = plot_df['age'].max()
    
    # Create bins like [18-23), [23-28), etc.
    bins = list(range(int(min_age), int(max_age) + bin_size, bin_size))
    labels = [f"{bins[i]}-{bins[i+1]}" for i in range(len(bins)-1)]
    
    plot_df['age_group'] = pd.cut(plot_df['age'], bins=bins, labels=labels, right=False)
    
    # 2. Calculate average for each group (for clean plotting)
    age_stats = plot_df.groupby('age_group', observed=False)['daily_active_minutes_instagram'].agg(['mean', 'count']).reset_index()
    
    # 3. Create figure
    fig, ax = plt.subplots(figsize=(12, 7))  # Wider figure for more groups
    
    # 4. Plot
    bars = ax.bar(age_stats['age_group'], age_stats['mean'], 
                  color=plt.cm.Set2(np.arange(len(age_stats))), 
                  edgecolor='black', width=0.7)
    
    # 5. Add NON-OVERLAPPING value labels
    # Strategy: Place labels above bars, offset if needed
    max_height = age_stats['mean'].max()
    label_offset = max_height * 0.03  # Small offset
    
    for i, (bar, count) in enumerate(zip(bars, age_stats['count'])):
        height = bar.get_height()
        
        # Position for label
        label_y = height + label_offset
        
        # Check for overlap with previous label
        if i > 0 and abs(height - age_stats.loc[i-1, 'mean']) < label_offset * 2:
            # If too close to previous bar's value, offset more
            label_y = height + label_offset * 2
        
        ax.annotate(f'{height:.1f}\n(n={count})',  # Show count too
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 5),  # 5 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom',
                   fontsize=9, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", 
                            facecolor="white", 
                            edgecolor="gray", 
                            alpha=0.8))
    
    # 6. Formatting
    ax.set_title(f"📱 Instagram Activity by Age Group ({bin_size}-Year Intervals)", 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel("Age Group", fontsize=13, labelpad=15)
    ax.set_ylabel("Average Daily Active Minutes", fontsize=13, labelpad=10)
    
    # 7. Improve x-axis readability
    ax.set_xticks(range(len(age_stats['age_group'])))
    ax.set_xticklabels(age_stats['age_group'], rotation=45, ha='right', fontsize=11)
    
    # 8. Grid and layout
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)  # Grid behind bars
    
    # Add a subtle horizontal line at y=0
    ax.axhline(y=0, color='black', linewidth=0.5)
    
    plt.tight_layout()
    return fig

def plot_dms_by_relationship_status(df):
    """DMs sent per week by Relationship Status"""
    if "weekly_work_hours" not in df.columns or "user_engagement_score" not in df.columns:
        return None
    fig, ax = plt.subplots(figsize=(9,6))
    ax = sns.barplot(x="relationship_status", y="dms_sent_per_week", data=df)
    ax.set_title("DMs Sent per Week by Relationship Status")
    ax.set_xlabel("Relationship Status")
    ax.set_ylabel("DMs Sent per Week")
    return fig

# 4. CORRELATION MATRIX FUNCTION
def plot_correlation_matrix(df):
    """Plots a heatmap of the correlation matrix."""
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.shape[1] < 2:
        return None
    corr = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', center=0, ax=ax)
    ax.set_title("Feature Correlation Matrix")
    return fig

# Add more functions for each visualization in your original script...
